"""Flat terrain environment configuration for hexapod."""

from isaaclab.utils import configclass
from isaaclab.terrains import TerrainImporterCfg
import isaaclab.sim as sim_utils
from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR

from .hexapod_env_cfg import HexapodEnvCfg


@configclass
class HexapodFlatEnvCfg(HexapodEnvCfg):
    def __post_init__(self):
        super().__post_init__()
        self.scene.terrain.terrain_type = "plane"
        self.scene.terrain.terrain_generator = None
        self.scene.height_scanner = None
        self.curriculum.terrain_levels = None
        self.scene.num_envs = 1024
        self.scene.env_spacing = 2.5


@configclass
class HexapodFlatEnvCfg_PLAY(HexapodFlatEnvCfg):
    def __post_init__(self):
        super().__post_init__()
        self.scene.num_envs = 1
        self.scene.env_spacing = 2.5
        self.episode_length_s = 40.0
        self.commands.base_velocity.resampling_time_range = (40.0, 40.0)
