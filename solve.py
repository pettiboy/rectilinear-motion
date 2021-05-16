import sympy

# for colored results
class c:
    HEADER = "\033[95m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    END = "\033[0m"


print(f"\n{c.CYAN}Following information required{c.END}....")

vertical_velocity = float(input("Vertical velocity in meters per second (m/s): "))
distance_from_ground = float(input("Distance from the ground in meters (m): "))

acceelaration = -9.81

# declare all symbols
t = sympy.Symbol("t")
y = sympy.Symbol("y")
v = sympy.Symbol("v")

print(f"\n\n{c.CYAN}Solving Problem{c.END}....\n")


# STEP 1 - integrate twice to find v(t) and y(t)
print(f"{c.HEADER}Integrating twice to find v(t) and y(t)....{c.END}")

v_of_t = vertical_velocity + sympy.integrate(acceelaration, t)
y_of_t = distance_from_ground + sympy.integrate(v_of_t, t)

print(
    f"{c.YELLOW}Velocity{c.END} above ground at time t, {c.GREEN}v(t) = {v_of_t}{c.END}"
)
print(
    f"{c.YELLOW}Elevation{c.END} above ground at time t, {c.GREEN}y(t) = {y_of_t}{c.END}",
    end="\n\n",
)

# STEP 2 - solve for t at which velocity is 0 and evaluate corresponding altitude
print(
    f"{c.HEADER}Solving for t at which velocity equals zero and evaluating corresponding altitude....{c.END}",
)

t_at_v0 = sympy.solve(v_of_t)[0]  # solve v_of_t = 0

y_eqn = sympy.Eq(y_of_t, y)  # y = y_of_t
t_eqn = sympy.Eq(t_at_v0, t)  # t = t_at_v0

y_value = sympy.solve((y_eqn, t_eqn), (y, t))

print(
    f"Highest {c.YELLOW}Elevation{c.END} reached by object {c.GREEN}{y_value[0][0]} meters{c.END}"
)
print(
    f"Coressponding {c.YELLOW}Time{c.END} {c.GREEN}{t_at_v0} seconds{c.END}", end="\n\n"
)


#  STEP 3 - solve for t at which altitude is 0 and evaluate corresponding velocity
print(
    f"{c.HEADER}Solving for t at which altitude is 0 and evaluating corresponding velocity.....{c.END}",
)

new_t = max(sympy.solve(sympy.Eq(y_of_t, 0), t))
print(
    f"{c.YELLOW}Time{c.END} when object will hit the ground {c.GREEN}{new_t} senconds{c.END}"
)

new_v = sympy.solve((sympy.Eq(v_of_t, v), sympy.Eq(new_t, t)), (v, t))
print(
    f"Coressponding {c.YELLOW}Velocity{c.END} {c.GREEN}{new_v[v]} meters/second{c.END}",
    end="\n\n",
)
