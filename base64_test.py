import base64

test_data = [
    ('Many hands make light work.', 'TWFueSBoYW5kcyBtYWtlIGxpZ2h0IHdvcmsu', 'utf-8'),
    ('Man', 'TWFu', 'utf-8'),
    ('Ma', 'TWE=', 'utf-8'),
    ('M', 'TQ==', 'utf-8'),
    ('Ā', 'xIA=', 'utf-8'),
    ('Many hands make light work.', 'AE0AYQBuAHkAIABoAGEAbgBkAHMAIABtAGEAawBlACAAbABpAGcAaAB0ACAAdwBvAHIAawAu', 'utf-16-be')
]

for data in test_data:
    test_input = data[0]
    expected_output = data[1]
    encoding = data[2]
    actual_output = base64.encode_text(test_input, encoding)
    if expected_output != actual_output:
        report = {'input': test_input, 'expected output': expected_output, 'actual output': actual_output}
        raise AssertionError(report)


for data in test_data:
    test_input = data[1]
    expected_output = data[0]
    encoding = data[2]
    actual_output = base64.decode_text(test_input, encoding)
    if expected_output != actual_output:
        report = {'input': test_input, 'expected output': expected_output, 'actual output': actual_output}
        raise AssertionError(report)

print('Success')
