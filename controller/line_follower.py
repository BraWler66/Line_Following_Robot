from controller import Robot

def run_robot(robot): 
    time_step = 32 
    max_speed = 6.28 

    # Left wheel motor 
    left_motor = robot.getMotor('left wheel motor') 
    left_motor.setPosition(float('inf')) 
    left_motor.setVelocity(0.0) 

    # Right wheel motor  
    right_motor = robot.getMotor('right wheel motor') 
    right_motor.setPosition(float('inf')) 
    right_motor.setVelocity(0.0) 

    # Distance sensors 
    left_ir = robot.getDistanceSensor('left ir') 
    left_ir.enable(time_step) 
    right_ir = robot.getDistanceSensor('right ir') 
    right_ir.enable(time_step) 

    while robot.step(time_step) != -1: 
        left_ir_value = left_ir.getValue() 
        right_ir_value = right_ir.getValue() 
        print(f"Left IR: {left_ir_value:.2f}, Right IR: {right_ir_value:.2f}") 

        # Default forward speed
        left_speed = max_speed * 0.25 
        right_speed = max_speed * 0.25 

        # Adjust speed based on IR sensor difference
        if left_ir_value > right_ir_value and left_ir_value > 15: 
            left_speed = max_speed * 0.2 
            right_speed = max_speed * 0.4 
        elif right_ir_value > left_ir_value and right_ir_value > 15: 
            left_speed = max_speed * 0.4 
            right_speed = max_speed * 0.2 

        left_motor.setVelocity(left_speed) 
        right_motor.setVelocity(right_speed) 

# Create robot instance and run
my_robot = Robot() 
run_robot(my_robot)
