from django import template

register = template.Library()


@register.filter(name='Censor')
def censor(value):

    Cens_List = ['idiot', 'stupid', 'donkey']
    sentence = value.split()

    for i in Cens_List:
        for words in sentence:
            if i in words:
                pos = sentence.index(words)
                sentence.remove(words)
                sentence.insert(pos, '*' * len(i))
            return " ".join(sentence)
