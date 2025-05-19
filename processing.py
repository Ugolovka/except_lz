import os
import pandas as pd


class DataProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.expected_columns = ['Участники гражданского оборота', 'Тип операции', 'Сумма операции', 'Вид расчета', 'Место оплаты', 'Терминал оплаты', 'Дата оплаты', 'Время оплаты', 'Результат операции', 'Cash-back', 'Сумма cash-back']
        self.expected_dtypes = {
            'Участники гражданского оборота': object,
            'Тип операции': object,
            'Сумма операции': float,
            'Вид расчета': object,
            'Место оплаты': object,
            'Терминал оплаты': object,
            'Дата оплаты': object,
            'Время оплаты': object,
            'Результат операции': object,
            'Cash-back':object,
            'Сумма cash-back':float
        }

    def read_dataframe(self):
        try:
            if not os.path.exists(self.filename):
                raise FileNotFoundError(f"[Errno 2] No such file or directory: '{self.filename}'")

            df = pd.read_csv(self.filename)

            if df.empty:
                raise ValueError("Датафрейм пуст")

            self._validate_structure(df)

            print("Чтение датафрейма завершено успешно.")
            return df

        except FileNotFoundError as e:
            print(f"Возникла следующая ошибка: {e}")

        except ValueError as e:
            print(f"Возникла следующая ошибка: {e}")

        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")

    def _validate_structure(self, df):
        errors = []

        if list(df.columns) != self.expected_columns:
            errors.append("- Названия столбцов не совпадают.")
            errors.append(f"Ожидаемые: {self.expected_columns}")
            errors.append(f"Фактические: {list(df.columns)}")

        for col, expected_type in self.expected_dtypes.items():
            if col in df.columns:
                actual_type = df[col].dropna().dtype

                expected_numpy_type = pd.Series(dtype=expected_type).dtype

                if actual_type != expected_numpy_type:
                    errors.append(f"В столбце '{col}' тип данных не соответствует ожидаемому.")
                    errors.append(f"Ожидается: {expected_numpy_type}, фактически: {actual_type}")



        if errors:
            print("Структура датафрейма НЕ соответствует ожидаемой:")
            for error in errors:
                print(error)
            raise ValueError("Файл не соответствует структуре")

