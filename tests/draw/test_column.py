"""Test how columns are drawn."""

from ..testing_utils import assert_no_logs


@assert_no_logs
def test_column_rule_1(assert_pixels):
    assert_pixels('''
        a_r_a
        a_r_a
        _____
    ''', '''
      <style>
        img { display: inline-block; width: 1px; height: 1px }
        div { columns: 2; column-rule-style: solid;
              column-rule-width: 1px; column-gap: 3px;
              column-rule-color: red }
        body { margin: 0; font-size: 0 }
        @page { margin: 0; size: 5px 3px }
      </style>
      <div>
        <img src=blue.jpg>
        <img src=blue.jpg>
        <img src=blue.jpg>
        <img src=blue.jpg>
      </div>''')


@assert_no_logs
def test_column_rule_2(assert_pixels):
    assert_pixels('''
        a_r_a
        a___a
        a_r_a
    ''', '''
      <style>
        img { display: inline-block; width: 1px; height: 1px }
        div { columns: 2; column-rule-style: dotted;
              column-rule-width: 1px; column-gap: 3px;
              column-rule-color: red }
        body { margin: 0; font-size: 0 }
        @page { margin: 0; size: 5px 3px }
      </style>
      <div>
        <img src=blue.jpg>
        <img src=blue.jpg>
        <img src=blue.jpg>
        <img src=blue.jpg>
        <img src=blue.jpg>
        <img src=blue.jpg>
      </div>''')
