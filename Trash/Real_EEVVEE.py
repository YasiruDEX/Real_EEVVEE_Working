bl_info = {
    "name": "Real EEVVEE",
    "author": "Yasiru Basnayake",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Render > Real EEVVEE",
    "description": "Make EEVVEE render engine realistic",
    "warning": "",
    "doc_url": "",
    "category": "Render",
}

import bpy

def QuickEffects(context):
    bpy.context.scene.eevee.use_gtao = True
    bpy.context.scene.eevee.use_ssr = True
    bpy.context.scene.eevee.use_bloom = True
    bpy.context.scene.view_settings.look = 'High Contrast'
    bpy.context.scene.eevee.use_motion_blur = True




class Quick_Effects(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Quick Effect"

    def execute(self, context):
        QuickEffects(context)
        return {'FINISHED'}
   
   
    
class RealEEVVEEPanel(bpy.types.Panel):
    
    bl_label = "Real EEVVEE"
    bl_idname = "RENDER_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        layout.label(text="Quick Effects:")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.simple_operator")


def register():
    bpy.utils.register_class(Quick_Effects)
    bpy.utils.register_class(RealEEVVEEPanel)


def unregister():
    bpy.utils.unregister_class(Quick_Effects)
    bpy.utils.unregister_class(RealEEVVEEPanel)
    
if __name__ == "__main__":
    register()
    
