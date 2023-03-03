import pytest

from consts import Const


@pytest.mark.parametrize(
    ('question', 'answer'),
    Const.FAQ_Q_A,
    ids=map(lambda i: f"question_{i}", range(len(Const.FAQ_Q_A))))
def test_faq(open_url, wait, home_page, question, answer):
    open_url()
    faq = home_page.faq
    assert faq.has(question)
    assert not faq.is_open(question)
    faq.open(question)
    wait.until(lambda driver: faq.is_open(question))
    assert faq.question_matches_answer(question, answer)

