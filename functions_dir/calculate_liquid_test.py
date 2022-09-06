import time

from selenium.webdriver.common.by import By

from functions_dir.base import Base

from . import constant as const

CALCULATE_LIQUID_TEST_URL = const.CALCULATE_LIQUID_TEST_URL


class CalculateLiquidTest(Base):
    def check_report_data_equal_zero(self):
        degree_of_dehydration = self.find_element(By.ID, "lblDehydrationResult")
        liquid_loss = self.find_element(By.ID, "lblFluidLossResult")
        liquid_loss_per_hour = self.find_element(By.ID, "lblHourlyFluidLossResult")
        intake_during_training = self.find_element(By.ID, "lblIntakeResult")
        additional_intake = self.find_element(By.ID, "lblAdditionalIntakeResult")

        if (
            (str(degree_of_dehydration.text.strip()) == "0")
            and (str(liquid_loss.text.strip()) == "0")
            and (str(liquid_loss_per_hour.text.strip()) == "0")
            and (str(intake_during_training.text.strip()) == "0")
            and (str(additional_intake.text.strip()) == "0")
        ):
            return True
        else:
            return False

    def fill_data(self):
        name = self.find_element(By.ID, "content_0_txtName")
        weight_before = self.find_element(By.ID, "txbStartWeight")
        weight_after = self.find_element(By.ID, "txbEndWeight")
        fluid_intake = self.find_element(By.ID, "txbFluidIntake")
        training_time = self.find_element(By.ID, "txbTrainTime")

        weight_before.send_keys("90")
        weight_after.send_keys("88.7")
        fluid_intake.send_keys("3.2")
        training_time.send_keys("109")
        name.send_keys("Dmitry")
        time.sleep(2)

    def check_report_data(self):
        degree_of_dehydration = self.find_element(By.ID, "lblDehydrationResult")
        liquid_loss = self.find_element(By.ID, "lblFluidLossResult")
        liquid_loss_per_hour = self.find_element(By.ID, "lblHourlyFluidLossResult")
        intake_during_training = self.find_element(By.ID, "lblIntakeResult")
        additional_intake = self.find_element(By.ID, "lblAdditionalIntakeResult")

        if (
            (str(degree_of_dehydration.text.strip()) == "0")
            or (str(liquid_loss.text.strip()) == "0")
            or (str(liquid_loss_per_hour.text.strip()) == "0")
            or (str(intake_during_training.text.strip()) == "0")
            or (str(additional_intake.text.strip()) == "0")
        ):
            return False
        else:
            return True
