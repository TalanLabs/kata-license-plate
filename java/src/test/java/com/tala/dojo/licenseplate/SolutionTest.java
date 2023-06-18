package com.tala.dojo.licenseplate;

import com.talan.dojo.licenseplate.Solution;
import org.junit.jupiter.api.*;
import org.junit.jupiter.api.Assertions;
public class SolutionTest {

    @Test
    @DisplayName("plus five")
    void plusFive() {
        // test case
        String currentLicensePlate = "AB-123-CD";
        int n = 5;
        // then
        String nextLicensePlate = Solution.nextLicensePlate(currentLicensePlate, n);
        Assertions.assertEquals(nextLicensePlate, "AB-128-CD");
    }

    @Test
    @DisplayName("plus one hundred")
    void plusOneHundred() {
        // test case
        String currentLicensePlate = "AZ-566-QS";
        int n = 100;
        // then
        String nextLicensePlate = Solution.nextLicensePlate(currentLicensePlate, n);
        Assertions.assertEquals(nextLicensePlate, "AZ-666-QS");
    }

    @Test
    @DisplayName("999 plus one")
    void plusOneWithJump() {
        // test case
        String currentLicensePlate = "BN-999-GH";
        int n = 1;
        // then
        String nextLicensePlate = Solution.nextLicensePlate(currentLicensePlate, n);
        Assertions.assertEquals(nextLicensePlate, "BN-001-GI");
    }

    @Test
    @DisplayName("plus ten thousand")
    void plusTenThousand() {
        // test case
        String currentLicensePlate = "CG-007-CG";
        int n = 10000;
        // then
        String nextLicensePlate = Solution.nextLicensePlate(currentLicensePlate, n);
        Assertions.assertEquals(nextLicensePlate, "CG-017-CQ");
    }

    @Test
    @DisplayName("plus one hundred thousand")
    void plusOneHundredThousand() {
        // test case
        String currentLicensePlate = "IO-010-OI";
        int n = 100000;
        // then
        String nextLicensePlate = Solution.nextLicensePlate(currentLicensePlate, n);
        Assertions.assertEquals(nextLicensePlate, "IO-110-SE");
    }

    @Test
    @DisplayName("plus one million")
    void plusOneMillion() {
        // test case
        String currentLicensePlate = "QS-456-DF";
        int n = 1000000;
        // then
        String nextLicensePlate = Solution.nextLicensePlate(currentLicensePlate, n);
        Assertions.assertEquals(nextLicensePlate, "QT-457-PS");
    }
}
