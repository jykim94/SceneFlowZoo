_base_ = ["../../pseudoimage.py"]

is_trainable = False
has_labels = False

test_dataset_root = "/efs/argoverse2/train/"
save_output_folder = "/efs/argoverse2/train_nsfp_flow/"

SEQUENCE_LENGTH = 2

model = dict(name="CacheWrapper",
             args=dict(model="NSFP",
                       args=dict(VOXEL_SIZE={{_base_.VOXEL_SIZE}},
                       POINT_CLOUD_RANGE={{_base_.POINT_CLOUD_RANGE}},
                       SEQUENCE_LENGTH=SEQUENCE_LENGTH)))

epochs = 20
learning_rate = 2e-6
save_every = 500
validate_every = 500

test_dataset = dict(name="BucketedSceneFlowDataset",
                    args=dict(dataset_name="Argoverse2SceneFlow",
                              root_dir=test_dataset_root,
                              with_ground=False,
                              with_rgb=False,
                              eval_type="bucketed_epe",
                              eval_args=dict()))

test_dataloader = dict(
    args=dict(batch_size=1, num_workers=1, shuffle=False, pin_memory=True))
