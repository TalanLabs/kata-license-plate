import { nextLicensePlate } from './license.plate'

describe('license plate', () => {
  test('plus five', () => {
    const licensePlate = nextLicensePlate('AB-123-CD', 5)
    expect('AB-128-CD').toEqual(licensePlate)
  })

  test('plus one hundred', () => {
    const licensePlate = nextLicensePlate('AZ-566-QS', 100)
    expect('AZ-666-QS').toEqual(licensePlate)
  })

  test('999 plus one', () => {
    const licensePlate = nextLicensePlate('BN-999-GH', 1)
    expect('BN-001-GI').toEqual(licensePlate)
  })

  test('plus ten thousand', () => {
    const licensePlate = nextLicensePlate('CG-007-CG', 10000)
    expect('CG-017-CQ').toEqual(licensePlate)
  })

  test('plus one hundred thousand', () => {
    const licensePlate = nextLicensePlate('IO-010-OI', 100000)
    expect('IO-110-SE').toEqual(licensePlate)
  })

  test('plus one million', () => {
    const licensePlate = nextLicensePlate('QS-456-DF', 1000000)
    expect('QT-457-PS').toEqual(licensePlate)
  })
})
