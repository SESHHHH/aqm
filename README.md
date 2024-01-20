# AQM

Расчёт показателей качества VQM: PESQ, CSIG, CBAK, COVL, SSNR.

Реализация MATLAB была взята из [https://ecs.utdallas.edu/loizou/speech/software.htm](https://ecs.utdallas.edu/loizou/speech/software.htm).

Консольная программа позволяет расчитывать показатели качества аудио в виде метрик PESQ, CSIG, CBAK, COVL, SSNR.
Оценки основаны на шкале MOS от 1 до 5.

# Использование

Для реализации расчёта метрик необходимо запустить файл main.py и указать путь к оригинальному аудиофайлу clean и к обработанному enhanced,
после чего в консоли отобразятся рассчитанные метрики.

# Requirements

1. Необходимо установить Octave для работы MATLAB: [octave.org](octave.org)
2. Добавить путь к Octave в PATH. Например, "C:\Program Files\GNU Octave\Octave-8.4.0\mingw64\bin"
3. `python setup.py install`
4. В случае возникновения ошибки ERROR: Could not build wheels for pesq, which is required to install pyproject.toml-based projects  
   Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools" необходимо установить Microsoft C++ Build Tools:
   [https://visualstudio.microsoft.com/ru/visual-cpp-build-tools/](https://visualstudio.microsoft.com/ru/visual-cpp-build-tools/). После устновки
   необходимо загрузить пакет "Разработка классических приложений на C++" размером 6 Гб.
5. В конечном счёте будут установлены следующие пакеты:  
   setuptools>=40.0.0  
   Cython  
   scipy  
   oct2py  
   pesq  
   sox  

# Источники

MATLAB ресурс: [https://ecs.utdallas.edu/loizou/speech/software.htm](https://ecs.utdallas.edu/loizou/speech/software.htm)

```bib
@ARTICLE{4389058,
  author={Y. {Hu} and P. C. {Loizou}},
  journal={IEEE Transactions on Audio, Speech, and Language Processing}, 
  title={Evaluation of Objective Quality Measures for Speech Enhancement}, 
  year={2008},
  volume={16},
  number={1},
  pages={229-238},
}
```
