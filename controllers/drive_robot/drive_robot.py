from controller import Robot

if __name__ == "__main__":
    # Create the Robot instance.
    robot = Robot()
    
    # Get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    speed_max = 6.28  # Maximum speed
    
    # Initialize devices
    motor_l = robot.getDevice("motor_1")
    motor_r = robot.getDevice("motor_2")
    camera = robot.getDevice("camera")
    keyboard = robot.getKeyboard()
    
    # Set motor initial configurations
    motor_l.setPosition(float('inf'))
    motor_l.setVelocity(0.0) 
    motor_r.setPosition(float('inf'))
    motor_r.setVelocity(0.0) 
    
    # Enable devices
    camera.enable(timestep)
    keyboard.enable(timestep)
    
    # Main loop: perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # Initialize motor speeds
        speed_l = 0.0
        speed_r = 0.0
        
        # Get keyboard input
        key = keyboard.getKey()
        
        # Define movement based on key pressed
        if key == ord('W') or key == keyboard.UP:
            # Move forward
            speed_l = 1.0 * speed_max
            speed_r = 1.0 * speed_max
        elif key == ord('S') or key == keyboard.DOWN:
            # Move backward
            speed_l = -1.0 * speed_max
            speed_r = -1.0 * speed_max
        elif key == ord('A') or key == keyboard.LEFT:
            # Turn left
            speed_l = -1.0 * speed_max
            speed_r = 1.0 * speed_max
        elif key == ord('D') or key == keyboard.RIGHT:
            # Turn right
            speed_l = 1.0 * speed_max
            speed_r = -1.0 * speed_max
        
        # Set motor speeds
        motor_l.setVelocity(speed_l)
        motor_r.setVelocity(speed_r)
    
    # Enter exit cleanup code here (if necessary).
