import gen_scale as gs
import simpleaudio as sa
import math

def bit_ref(i,index):
    return (i & (1 << index)) >> index

def decode_config(seed):
    ret = {}
    ret["speedup"] = []
    ret["is_desc"] = []
    ret["is_arpeg"] = []
    ret["is_minor"] = []
    for i in range(8):
        ret["speedup"].append(bit_ref(seed,i))
    for i in range(8,16):
        ret["is_desc"].append(bit_ref(seed,i))
    for i in range(16,24):
        ret["is_arpeg"].append(bit_ref(seed,i))
    for i in range(24,32):
        ret["is_minor"].append(bit_ref(seed,i))
    return ret

def next_scale(this_scale,layer,config,i):
    next_scale_width = round(math.log2(this_scale.note_alignment)) - config["speedup"][layer]
    next_scale_root = this_scale.note_list[i % len(this_scale.note_list)]
    next_scale_root_note = next_scale_root.major_note
    next_scale_octave = next_scale_root.octave+config["speedup"][layer] % 9
    next_scale_is_desc = config["is_desc"][layer]
    next_scale_is_arpeg = config["is_arpeg"][layer]
    next_scale_is_minor = config["is_minor"][layer]
    ret = gs.scale(0,next_scale_root_note,next_scale_octave,next_scale_width, next_scale_is_desc)
    if(next_scale_is_minor):
        ret.minor()
    else:
        ret.major()
    if(next_scale_is_arpeg):
        ret.arpegio()
    ret.repeat(2 - next_scale_width)
    return ret

def make_bar(i,main_scale,num_scales,config):
    scale_list = [main_scale]
    for j in range(1,i):
        scale_list.append(next_scale(scale_list[-1],j,config,i))
    return gs.mix_scales(scale_list,44100)

keep_playing = 1

def make_music(main_is_arpeg,main_root_note,main_octave,main_is_desc,main_is_minor,num_scales,seed):
    config = decode_config(seed)
    main_scale = gs.scale(0,main_root_note,main_octave,3,main_is_desc)
    if(main_is_minor):
        main_scale.minor()
    else:
        main_scale.major()
    if(main_is_arpeg):
        main_scale.arpegio()
    play_obj = sa.play_buffer(make_bar(0,main_scale,num_scales,config),1,2,44100)
    i = 0
    while(keep_playing):
        while(1):
            try:
                i+= 1
                next_bar = make_bar(i,main_scale,num_scales,config)
                break
            except:
                continue
        play_obj.wait_done()
        play_obj = sa.play_buffer(make_bar(0,main_scale,num_scales,config),1,2,44100)
