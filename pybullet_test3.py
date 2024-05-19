import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
p.setTimeStep(1/200)
planeID = p.loadURDF("samurai.urdf")
cubeStartPos = [2, -1, 1]
cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 3.14])
robotID = p.loadURDF("robot2.urdf", cubeStartPos, cubeStartOrientation)
#robot 청소기 urdf file path 내에 있어야 load 가능


for i in range(10000):
    p.stepSimulation()
    time.sleep(1 / 200)

p.disconnect(physicsClient)