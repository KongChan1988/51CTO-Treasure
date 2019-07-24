#任务二：在词汇表中添加5个Python术语，在次运行程序时，这些新术语会在打印中输出
from collections import defaultdict
print('\n任务二：')
programming_languages = {'java':'面向对象的编程语言',
                        'c++':'面向过程的编程语言',
                        'python':'面向对象的编程语言',
                        'sql':'数据库查询语句',
                        'vbs':'HelloWorld脚本语言',
                        'python':['列表','元组','字典','类','继承']
                        }
#programming_languages['python']='字典'
programming_languages = defaultdict(set)
programming_languages['python'].add('多态')
for language,meaning in programming_languages.items():
    if language == 'python':
        print(str(language.title()) + '术语: ' + str(meaning))
    else:
        print(str(language.title()) + '含义： ' + str(meaning))
