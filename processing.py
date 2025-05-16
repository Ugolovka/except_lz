import os
import pandas as pd


class DataProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.expected_columns = ['A', 'B', 'C', 'D']
        self.expected_dtypes = {
            'A': int,
            'B': str,
            'C': float,
            'D': float
        }

    def read_dataframe(self):
        try:
            if not os.path.exists(self.filename):
                raise FileNotFoundError(f"[Errno 2] No such file or directory: '{self.filename}'")

            df = pd.read_csv(self.filename)

            if df.empty:
                raise ValueError("Датасет пуст")

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
                actual_type = df[col].dropna().map(type).mode()[0] if not df[col].dropna().empty else None
                if actual_type != expected_type:
                    errors.append(f"В столбце '{col}' тип данных не соответствует ожидаемому.")
                    errors.append(f"Ожидается: {expected_type.__name__}, фактически: {actual_type.__name__ if actual_type else 'пусто'}")

        if errors:
            print("Структура датафрейма НЕ соответствует ожидаемой:")
            for error in errors:
                print(error)
            raise ValueError("Файл не соответствует структуре")


if __name__ == "__main__":
    processor = DataProcessor("var9.csv")
    processor.read_dataframe()


