
import os
import pandas as pd

class DatasetChecker:
    def __init__(self, dataset_path, expected_columns):
        """Инициализация с путем к датасету и ожидаемой структурой"""
        self.dataset_path = dataset_path
        self.expected_columns = expected_columns

    def check_dataset(self):
        """Проверяет наличие датасета, его структуру и обрабатывает ошибки"""
        try:
            if not os.path.exists(self.dataset_path):
                raise FileNotFoundError(f"Файл {self.dataset_path} не найден.")

            df = pd.read_csv(self.dataset_path)

            if list(df.columns) != self.expected_columns:
                raise ValueError(f"Структура датасета не соответствует ожидаемой. Ожидалось: {self.expected_columns}, получено: {list(df.columns)}")

            print("✅ Датасет успешно проверен и соответствует ожидаемой структуре.")
            return df

        except FileNotFoundError as e:
            print(f"❌ Ошибка: {e}")

        except ValueError as e:
            print(f"❌ Ошибка: {e}")

        except Exception as e:
            print(f"❌ Неожиданная ошибка: {e}")

        return None

dataset_path = "var9.csv"
expected_columns = ["name", "age", "score"]

checker = DatasetChecker(dataset_path, expected_columns)
df = checker.check_dataset()
