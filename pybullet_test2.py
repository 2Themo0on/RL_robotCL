import os
import pybullet as p
import time
import pybullet_data


p.connect(p.GUI)
urdfRootPath = pybullet_data.getDataPath()
pandaUid = p.loadURDF(os.path.join(pybullet_data.getDataPath(),"franka_panda/panda.urdf"),useFixedBase=True)


#robot, tray올려둘 table 로딩
tableUid = p.loadURDF(os.path.join(urdfRootPath, "table/table.urdf"), basePosition = [0.5,0,-0.65])

p.setGravitiy(0,0,-10)
objecUid = p.loadURDF(os.path.join(urdfRootPath, "random_urdfs/000/000.urdf"),basePosition = [0.7,0,0.1])

while True:
    p.stepSimulation()
