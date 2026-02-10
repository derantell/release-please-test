using Monorepo.CoreLib;

namespace CoreLib.Tests;

public class CalculatorTests
{
    private readonly Calculator _calculator = new();

    [Test]
    [Arguments(2, 3, 5)]
    [Arguments(-1, 1, 0)]
    [Arguments(0, 0, 0)]
    public async Task Add_ReturnsSum(int a, int b, int expected)
    {
        await Assert.That(_calculator.Add(a, b)).IsEqualTo(expected);
    }

    [Test]
    [Arguments(5, 3, 2)]
    [Arguments(0, 1, -1)]
    public async Task Subtract_ReturnsDifference(int a, int b, int expected)
    {
        await Assert.That(_calculator.Subtract(a, b)).IsEqualTo(expected);
    }

    [Test]
    [Arguments(3, 4, 12)]
    [Arguments(-2, 5, -10)]
    [Arguments(0, 100, 0)]
    public async Task Multiply_ReturnsProduct(int a, int b, int expected)
    {
        await Assert.That(_calculator.Multiply(a, b)).IsEqualTo(expected);
    }

    [Test]
    [Arguments(10, 2, 5.0)]
    [Arguments(7, 2, 3.5)]
    public async Task Divide_ReturnsQuotient(int a, int b, double expected)
    {
        await Assert.That(_calculator.Divide(a, b)).IsEqualTo(expected);
    }

    [Test]
    public async Task Divide_ByZero_Throws()
    {
        await Assert.That(() => _calculator.Divide(1, 0))
            .Throws<DivideByZeroException>();
    }
}
