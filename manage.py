# -*- coding: utf-8 -*-
from flask.ext.script import Manager
from webapp.app import app

manager = Manager(app)

@manager.command
def hello():
    """
    Print hello
    """
    get_logger().debug("Hello debug")
    get_logger().info("Hello info")
    get_logger().warning("Hello warning")
    get_logger().error("Hello error")
    get_logger().critical("Hello critical")
    print "hello"


if __name__ == "__main__":
    manager.run()
