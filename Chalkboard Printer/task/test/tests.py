from hstest import StageTest, CheckResult, dynamic_test, TestedProgram


class Feedback:
    contain_msg = "Your output should contain the following message:\n"
    repeat_msg = "You should repeat the message as given times. Your repeat number: "
    wait_input = "Your program should wait for user input."


class ChalkboardPrinterTest(StageTest):
    prompts = [
        {"name": "Bart",
         "surname": "Simpson",
         "msg": "I will not skateboard in the halls.",
         "repeat": "20"},
        {"name": "Homer",
         "surname": "Simpson",
         "msg": "I will not teach others to fly.",
         "repeat": "30"},
        {"name": "Lisa",
         "surname": "Simpson",
         "msg": "I will not bring sheep to class.",
         "repeat": "40"},
        {"name": "Marge",
         "surname": "Simpson",
         "msg": "I will not eat things for money.",
         "repeat": "50"},
        {"name": "Maggie",
         "surname": "Simpson",
         "msg": "I will not hide the teacher's medication.",
         "repeat": "60"}
    ]

    # test if the output is correct
    @dynamic_test(data=prompts)
    def test1(self, prompt):
        main = TestedProgram(self.source_name)
        main.start()
        message = f"This is {prompt['name']} {prompt['surname']} and {prompt['msg']}"
        if main.is_waiting_input():
            main.execute(prompt['name'])
            if not main.is_waiting_input():
                return CheckResult.wrong(Feedback.wait_input)

            main.execute(prompt['surname'])
            if not main.is_waiting_input():
                return CheckResult.wrong(Feedback.wait_input)

            main.execute(prompt['msg'])
            if not main.is_waiting_input():
                return CheckResult.wrong(Feedback.wait_input)

            output = main.execute(prompt['repeat'])
            if message.strip() not in output.strip():
                return CheckResult.wrong(Feedback.contain_msg + message)

            # test if the message is repeated given times
            repeated_msg = output.strip().split("\n")
            if len(repeated_msg) != int(prompt['repeat']):
                return CheckResult.wrong(Feedback.repeat_msg + str(len(repeated_msg)))
            return CheckResult.correct()

        else:
            return CheckResult.wrong(Feedback.wait_input)


if __name__ == '__main__':
    ChalkboardPrinterTest('task').run_tests()
