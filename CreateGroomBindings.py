import unreal
from unreal import AssetData

def CreateGroomBindings(TargetSkel, GroomDir, SourceSkel):
    # Load the skeletal mesh asset
    skeletal_mesh = unreal.load_asset(TargetSkel)
    skeletal_src_mesh = unreal.load_asset(SourceSkel)

    # Verify that the target asset was loaded correctly
    if skeletal_mesh is not None:
        print("Skeletal mesh loaded successfully!")
    else:
        print("Failed to load the skeletal mesh.")

    reg = unreal.AssetRegistryHelpers.get_asset_registry()

    filt = unreal.ARFilter(
        package_paths=[GroomDir],
        class_names=["GroomAsset"],
    )

    groom_assets = reg.get_assets(filt)
    num=len(groom_assets)
    text = f"Found {num} groom_assets"
    unreal.log(text)

    print(groom_assets)

    for asset_data in groom_assets:
        obj = asset_data.get_asset()
        if obj:
            task = unreal.GroomLibrary()
            task.create_new_groom_binding_asset(obj, skeletal_mesh, num_interpolation_points=100,source_skeletal_mesh_for_transfer=skeletal_src_mesh, matching_section=0)
    
    print("completed groom bindings")