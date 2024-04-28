from hstest import StageTest, CheckResult, dynamic_test, TestedProgram


class Feedback:
    contain_msg = "Your output should contain the following message:\n"
    repeat_msg = "You should repeat the message 5 times. Your repeat number: "


class ChalkboardPrinterTest(StageTest):
    message = "This is Bart Simpson and I will not skateboard in the halls."

    # test if the output is correct
    @dynamic_test
    def test1(self):
        main = TestedProgram(self.source_name)
        output = main.start()
        if self.message.strip() not in output.strip():
            return CheckResult.wrong(Feedback.contain_msg + self.message)

        # test if the message is repeated 5 times
        repeated_msg = output.strip().split("\n")
        if len(repeated_msg) != 5:
            return CheckResult.wrong(Feedback.repeat_msg + str(len(repeated_msg)))
        return CheckResult.correct()


if __name__ == '__main__':
    ChalkboardPrinterTest('task').run_tests()
