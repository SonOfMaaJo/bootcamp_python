class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        summ = 0
        for coef, word in zip(coefs, words):
            summ += coef * len(word)
        return summ

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        summ = 0
        for idx, word in enumerate(words):
            summ += coefs[idx] * len(word)
        return summ
