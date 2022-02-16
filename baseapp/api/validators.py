import re

from zxcvbn import zxcvbn


def checkUname(uname):
    # TODO: why use r"" ?
    if not re.match(r"^[a-zA-Z0-9]{3,10}$", uname):
        return "Username must be alphanumeric, with 3 to 10 characters."


# TODO: more robust password checking
# const checkPassword = () =>
#     checkUtil(
#         () => {
#             const numsymbols = (password.match(/[!@#$%^&*`~]/g) || []).length;
#             const numdigits = (password.match(/[0-9]/g) || []).length;
#             const numcaps = (password.match(/[A-Z]/g) || []).length;
#             return (
#                 password.length >= 8 &&
#                 numdigits + numsymbols >= 3 &&
#                 numcaps >= 3 &&
#                 password.trim().toLocaleLowerCase() !== username.trim().toLowerCase()
#             );
#         },
#         `Here we go...
#         Password must not be same as username,
#         must contain minimum 3 symbols(including number(s)), and
#         at least 3 capital letters,
#         minimum length: 8.
#         Symbols include: !@#$%^&*\`~ only.`,
#         setPasswordError
#     );


def checkPassword(password, username, firstname, lastname, email):
    userInputs = [username, firstname, lastname, email]
    if not zxcvbn(password, user_inputs=userInputs)["score"] >= 3:
        return "Please choose a stronger password."


def checkConfPassword(password, confPassword):
    if password != confPassword:
        return "Passwords must match!"


def checkFirstname(firstname):
    if len(firstname) == 0:
        return "First name is required."


def checkLastname(lastname):
    if len(lastname) == 0:
        return "Last name is required."


def checkAdd1(add1):
    if len(add1) == 0:
        "This field is required."


def checkAdd2(add2):
    if len(add2) == 0:
        "This field is required."


def checkUserState(userState):
    if len(userState) == 0:
        "This field is required."


def checkCity(city):
    if len(city) == 0:
        "This field is required."


def checkPincode(pincode):
    if len(pincode) == 0:
        "This field is required."


def checkLandmark(landmark):
    if len(landmark) == 0:
        "This field is required."


def checkEmail(email):
    # TODO: copied regex... propbably this should work :)
    emailRegex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if not re.match(emailRegex, email):
        return "Please enter a valid email."
