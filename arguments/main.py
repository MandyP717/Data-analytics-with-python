# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line


def greet(name, template="Hello, <name>!"):
    return template.replace("<name>", name)


def force(mass, body="earth"):
    gravity_planet = {
        "sun": 274,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6,
    }
    return mass * gravity_planet[body.lower()]


def pull(m1, m2, d):
    force_pull = 6.674 * 10 ** -11 * ((m1 * m2) / d ** 2)
    return force_pull


# print(greet("Ewan", "What's up <name>!"))
# print(force(10, "pluto"))
# print(pull(0.1, 5.972 * pow(10, 24), 6.371 * pow(10, 6)))
