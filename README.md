# Rectilinear Motion

## What does it do?
This python program solves a simple mechanics problem of the type:
> Given `velocity` (vertical velocity in meters per sencond) and `height` (above the ground in meters) from which an object is dropped.
> 1. Calculate its velocity and elevation at any time `t`.
> 2. Its `highest elevation` and coressponding time.
> 3. Time and velocity with which it `hits the ground`.

## Question example
> Ball tossed with 10 m/s vertical velocity from window 20 m above ground.
> Determine:
> - velocity and elevation above ground at time t.
> - highest elevation reached by ball and coressponding time.
> - time when ball will hit the ground and corresponding velocity.


### Output in terminal
```
Solving Problem....

Integrating twice to find v(t) and y(t)....
Velocity above ground at time t, v(t) = 10.0 - 9.81*t
Elevation above ground at time t, y(t) = -4.905*t**2 + 10.0*t + 20.0

Solving for t at which velocity equals zero and evaluating corresponding altitude....
Highest Elevation reached by object 25.0968399592253 meters
Coressponding Time 1.01936799184506 seconds

Solving for t at which altitude is 0 and evaluating corresponding velocity.....
Time when object will hit the ground 3.28135452367464 senconds
Coressponding Velocity -22.1900878772482 meters/second
```

## Usage
```
git clone https://github.com/pettiboy/rectilinear-motion
pip install -r requirements.txt
python solve.py
```