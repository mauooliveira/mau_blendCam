#--------------------------------------------------
# mau_blendCam.py
# version: 0.0.1
# last updated: 15.05.22 (DD.MM.YY)
#--------------------------------------------------

# pending: adapt code to Transform

import nuke

def blendCam():
    #empty list for selected nodes
    selnodes = []

    #adding selected nodes into list
    for i in nuke.selectedNodes():
        selnodes.append(i.name())

    #defining ORIGIN and DESTINATION based or order of selection 
    orig = selnodes[-1]
    dest = selnodes[0]

    #creating new Camera
    blendCam = nuke.nodes.Camera2()

    #defining node colour
    blendCam_r = 0.055
    blendCam_g = 0.169
    blendCam_b = 0.243
    hexColour = int('%02x%02x%02x%02x' % (blendCam_r*255,blendCam_g*255,blendCam_b*255,1),16)
    blendCam.knob('tile_color').setValue(hexColour)

    #creating new slider knob and adding into Camera
    weight = nuke.Double_Knob('weight','weight')
    blendCam.addKnob(weight)

    #adding expression into Camera's translation, rotation and focal length
    blendCam.knob('translate').setExpression('((1-weight)*'+orig+'.translate)-('+dest+'.translate*-1*weight)')
    blendCam.knob('rotate').setExpression('((1-weight)*'+orig+'.rotate)-('+dest+'.rotate*-1*weight)')
    blendCam.knob('focal').setExpression('((1-weight)*'+orig+'.focal)-('+dest+'.focal*-1*weight)')
    blendCam.knob('haperture').setExpression('((1-weight)*'+orig+'.haperture)-('+dest+'.haperture*-1*weight)')
    blendCam.knob('vaperture').setExpression('((1-weight)*'+orig+'.vaperture)-('+dest+'.vaperture*-1*weight)')

    #adding new label into Camera
    blendCam.knob('label').setValue('\n'+'BlendCam'+'\n'+'\n'+orig+' <---> '+dest)


# add the following to menu.py
#===================================================================================================================
# MAU BLEND CAM
#===================================================================================================================
#import mau_blendCam
#mauMenu.addCommand('comp/blendCam','mau_blendCam.blendCam()')
