import torch
import matplotlib.pyplot as plt

x = torch.linspace(0, 30, 1000, requires_grad=True)
y = torch.sin(x) * x
y.backward(torch.ones_like(x))

plt.plot(x.detach().numpy(), y.detach().numpy(), label='Функция y=sin(x)*x')
plt.plot(x.detach().numpy(), x.grad.detach().numpy(), label='Производная данной функции')

plt.legend()
plt.show()