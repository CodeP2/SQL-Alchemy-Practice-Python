def data_convertion_error_message(err, user_input, example):
    print(f"""\r#########Error###########
          \r#Incorrect format -> {err}
          \r#Your's Input: >{user_input}<
          \r#Example: {example}
          \r##########################
          """)
    input("Press enter to continue...")


def integer_error_massage(user_input, options):
    print(f"""\r#########Error###########
          \r#The input is not a number!
          \r#Your input: {user_input}
          \r#Example of a correct input: 1
          \r##########################
          """)
    input("Press enter to continue...")
