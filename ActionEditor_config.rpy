init 1600 python in _viewers:
    #this is used for default transition
    #デフォルトで使用されるトランジションの文字列です。Noneも指定可能です。
    default_transition = "dissolve"
init -1600 python in _viewers:
    #hide winodw during animation in clipboard data
    #アニメーション中ウィンドウを隠すようにクリップボードを出力するか決定します
    hide_window_in_animation = True
    #If this is True and hide_window_in_animation is True, allow animation to be skipped
    #アニメーションをスキップできる形式でクリップボードに出力します。hide_window_in_animationがTrueのとき動作します。
    allow_animation_skip = True
    #this is used for default warper
    #デフォルトで使用されるwarper関数名の文字列を指定します。
    default_warper = "linear"
    # If True, show rot default.
    #True, なら格子をデフォルトで表示します。
    default_rot = False
    # If True, simulate defpth of field and focusing is enable by default.
    # Trueならカメラブラーを再現するフォーカシングをデフォルトで有効にします。
    default_show_camera_icon = True
    # If True, show camera icon which is dragged to move camera by default
    # Trueならドラッグでカメラを移動できるアイコンをデフォルトで表示します。
    default_one_line_one_prop = False
    # If True, One line includes only one property in clipboard data
    # Trueならクリップボードデータで一行に1つのプロパティーのみ記述します。
    default_legacy_gui = False
    # If True, use legacy action editor screen
    # Trueなら以前のレイアウトでActionEditorを表示します。
    focusing = False
    # If True, set camera keymap FPS(wasd), otherwise vim(hjkl)
    #Trueなら、カメラはWASD, wasdで、Falseならhjkl, HJKLで移動します。
    fps_keymap = False
    # the number of tabs shown at onece.
    #一度に表示する画像タグ数を設定します。
    tab_amount_in_page = 5
    #The blur value where the distance from focus position is dof.
    #フォーカシングでフォーカス位置からDOF離れた場所でのブラー量を設定します。
    _camera_blur_amount = 2.0 
    #warper function name which is used for the distance from focus position and blur amount.
    #フォーカス位置からの距離とカメラブラーの効きを決定するwarper関数名の文字列です
    _camera_blur_warper = "linear" 
    # the range of values of properties for int type
    #エディターのバーに表示する整数の範囲です。
    wide_range = 1500
    # the range of values of properties for float type
    #エディターのバーに表示する浮動小数の範囲です。
    narrow_range = 7.0
    # the range of time
    #エディターのバーに表示する時間の範囲です。
    time_range = 7.0

    preview_size=0.6
    preview_background_color="#111"


    props_set = [
        ("child", "xpos", "ypos", "zpos", "rotate"), 
        ("offsetX", "offsetY", "offsetZ", "rotateX", "rotateY", "rotateZ"),
        ("xanchor", "yanchor", "matrixanchorX", "matrixanchorY", "xoffset", "yoffset"), 
        ("xzoom", "yzoom", "zoom", "cropX", "cropY", "cropW", "cropH"), 
        ("alpha", "blur", "additive", "invert", "contrast", "saturate", "bright", "hue", "dof", "focusing")
    ]
    props_set_names = [
        "Child/Pos    ", 
        "3D Matrix    ",
        "Anchor/Offset", 
        "Zoom/Crop    ", 
        "Effect       "
    ]

    props_groups = {
        "matrixtransform":["rotateX", "rotateY", "rotateZ", "offsetX", "offsetY", "offsetZ"], 
        "matrixanchor":["matrixanchorX", "matrixanchorY"], 
        "matrixcolor":["invert", "contrast", "saturate", "bright", "hue"], 
        "crop":["cropX", "cropY", "cropW", "cropH"], 
        "focusing":["focusing", "dof"], 
    }

    special_props = ["child"]

    force_float = ["zoom", "xzoom", "yzoom", "alpha", "additive", "blur", "invert", "contrast", "saturate", "bright"]
    force_wide_range = ["rotate", "rotateX", "rotateY", "rotateZ", "offsetX", "offsetY", "offsetZ", "zpos", "xoffset", "yoffset", "hue", "dof", "focusing"]
    force_plus = ["additive", "blur", "alpha", "invert", "contrast", "saturate", "cropW", "cropH", "dof", "focusing"]
    #crop doesn't work when perspective True and rotate change the pos of image when perspective is not True
    not_used_by_default = ["rotate", "cropX", "cropY", "cropW", "cropH"]

    sort_ref_list = [
    "pos",
    "anchor",
    "offset",
    "xpos", 
    "xanchor", 
    "xoffset", 
    "ypos", 
    "yanchor", 
    "yoffset", 
    "zpos", 
    "matrixtransform", 
    "matrixanchor", 
    "rotate", 
    "xzoom", 
    "yzoom", 
    "zoom", 
    "crop", 
    "alpha", 
    "additive", 
    "blur", 
    "matrixcolor", 
    ]

    xygroup = {"pos": ("xpos", "ypos"), "anchor": ("xanchor", "yanchor"), "offset": ("xoffset", "yoffset")}

init 1600 python in _viewers:
    transform_props = (
    ("child", (None, None)), 
    ("xpos", 0.5), 
    ("ypos", 1.), 
    ("zpos", 0.), 
    ("xanchor", 0.5), 
    ("yanchor", 1.), 
    ("matrixanchorX", 0.5), 
    ("matrixanchorY", 0.5), 
    ("xoffset", 0), 
    ("yoffset", 0), 
    ("rotate", 0,),
    ("xzoom", 1.), 
    ("yzoom", 1.), 
    ("zoom", 1.), 
    ("cropX", 0.), 
    ("cropY", 0.), 
    ("cropW", 1.), 
    ("cropH", 1.), 
    ("offsetX", 0.),
    ("offsetY", 0.),
    ("offsetZ", 0.),
    ("rotateX", 0.),
    ("rotateY", 0.),
    ("rotateZ", 0.),
    ("dof", 400),
    ("focusing", renpy.config.perspective[1]), 
    ("alpha", 1.), 
    ("additive", 0.), 
    ("blur", 0.), 
    ("hue", 0.), 
    ("bright", 0.), 
    ("saturate", 1.), 
    ("contrast", 1.), 
    ("invert", 0.), 
    ("zzoom", False)
    )

    #perspetve competes crop
    camera_props = (
    ("xpos", 0.), 
    ("ypos", 0.), 
    ("zpos", 0.), 
    ("xanchor", 0.), 
    ("yanchor", 0.), 
    ("matrixanchorX", 0.5), 
    ("matrixanchorY", 0.5), 
    ("xoffset", 0), 
    ("yoffset", 0), 
    ("rotate", 0,),
    ("xzoom", 1.), 
    ("yzoom", 1.), 
    ("zoom", 1.), 
    ("cropX", 0.), 
    ("cropY", 0.), 
    ("cropW", 1.), 
    ("cropH", 1.), 
    ("offsetX", 0.),
    ("offsetY", 0.),
    ("offsetZ", 0.),
    ("rotateX", 0.),
    ("rotateY", 0.),
    ("rotateZ", 0.),
    ("dof", 400),
    ("focusing", renpy.config.perspective[1]), 
    ("alpha", 1.), 
    ("additive", 0.), 
    ("blur", 0.), 
    ("hue", 0.), 
    ("bright", 0.), 
    ("saturate", 1.), 
    ("contrast", 1.), 
    ("invert", 0.), 
    ("perspective", None)
    )
