from poppy.creatures import AbstractPoppyCreature


class PoppyErgoStarter(AbstractPoppyCreature):
    @classmethod
    def setup(cls, robot):
        for m in robot.motors:
            m.goto_behavior = 'dummy'

        #robot.attach_primitive(Jump(robot), 'jump')
        #print "robot is setup"
        