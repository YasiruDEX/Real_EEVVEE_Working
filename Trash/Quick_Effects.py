import bpy

class Quick_Effects(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Quick Optimize"

    def execute(self, context):
        QuickEffects(context)
        return {'FINISHED'}
    

    

    
        