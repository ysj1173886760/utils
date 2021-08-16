for i in range(1, 19):
    s = "{{ Common::KEYCODE_F{},\t\t\t0x{:X} }}, ".format(i, 0x6F + i)
    print (s)