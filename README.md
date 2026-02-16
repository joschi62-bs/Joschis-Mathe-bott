import sympy as sp

def algebra_example():
    # Algebra: Solving equations
    x = sp.symbols('x')
    equation = sp.Eq(x**2 + 2*x + 1, 0)
    solution = sp.solve(equation, x)
    return solution

def geometry_example():
    # Geometry: Area of a circle
    radius = sp.symbols('r')
    area = sp.pi * radius**2
    return area

def trigonometry_example():
    # Trigonometry: sin, cos and tan
    x = sp.symbols('x')
    sin_x = sp.sin(x)
    cos_x = sp.cos(x)
    return sin_x, cos_x

def analysis_example():
    # Analysis: Derivative
    x = sp.symbols('x')
    f = x**2
    derivative = sp.diff(f, x)
    return derivative

def linear_algebra_example():
    # Linear Algebra: Matrix operations
    A = sp.Matrix([[1, 2], [3, 4]])
    B = sp.Matrix([[5, 6], [7, 8]])
    product = A * B
    return product

def statistics_example():
    # Statistics: Expected value, variance
    x = sp.symbols('x')
    probability_distribution = sp.DiracDelta(x)
    expected_value = sp.integrate(x * probability_distribution, (x, -sp.oo, sp.oo))
    variance = sp.integrate((x - expected_value)**2 * probability_distribution, (x, -sp.oo, sp.oo))
    return expected_value, variance

def complex_numbers_example():
    # Complex Numbers: Operations
    z1 = sp.sympify('2 + 3*I')
    z2 = sp.sympify('1 - 4*I')
    addition = z1 + z2
    multiplication = z1 * z2
    return addition, multiplication

def differential_equations_example():
    # Differential Equations: Solve dy/dx = y
    y = sp.Function('y')(x)
    differential_eq = sp.Eq(y.diff(x), y)
    solution = sp.dsolve(differential_eq, y)
    return solution

def main():
    print("Algebra Example:", algebra_example())
    print("Geometry Example:", geometry_example())
    print("Trigonometry Example:", trigonometry_example())
    print("Analysis Example:", analysis_example())
    print("Linear Algebra Example:", linear_algebra_example())
    print("Statistics Example:", statistics_example())
    print("Complex Numbers Example:", complex_numbers_example())
    print("Differential Equations Example:", differential_equations_example())

if __name__ == '__main__':
    main()
	 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat Interface</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #1f1f1f;
            color: #ffffff;
            margin: 0;
            padding: 0;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
            height: 100vh;
            overflow: hidden;
        }
        .chat-box {
            flex: 1;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
            padding: 10px;
            background-color: #2c2c2c;
        }
        .message {
            margin: 10px 0;
            padding: 10px;
            border-radius: 5px;
        }
        .message.user {
            background-color: #3a3a3a;
            align-self: flex-end;
        }
        .message.bot {
            background-color: #4a4a4a;
        }
        .input-container {
            display: flex;
            padding: 10px;
            background-color: #2c2c2c;
        }
        .input-container input {
            flex: 1;
            padding: 10px;
            border: none;
            border-radius: 5px;
            margin-right: 10px;
        }
        .toggle-darkmode {
            cursor: pointer;
            background: none;
            border: none;
            color: #fff;
            font-size: 20px;
            margin-right: 10px;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-box" id="chatBox">
            <!-- Chat messages will be appended here -->
        </div>
        <div class="input-container">
            <button class="toggle-darkmode" onclick="toggleDarkMode()"><i class="fas fa-moon"></i></button>
            <input type="text" id="userInput" placeholder="Type a message...">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS_HTML"></script>
    <script>
        const chatBox = document.getElementById('chatBox');

        function sendMessage() {
            const input = document.getElementById('userInput');
            const message = input.value;
            if (message.length === 0) return;

            appendMessage('user', message);
            input.value = '';

            // Simulate bot response
            setTimeout(() => {
                const botResponse = 'Bot reply to: ' + message;
                appendMessage('bot', botResponse);
                MathJax.Hub.Queue(['Typeset', MathJax.Hub, chatBox]);
            }, 1000);
        }

        function appendMessage(sender, message) {
            const messageDiv = document.createElement('div');
            messageDiv.classList.add('message', sender);
            messageDiv.innerHTML = message;
            chatBox.appendChild(messageDiv);
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        function toggleDarkMode() {
            document.body.classList.toggle('dark-mode');
            // Change background and text color for dark mode
        }

    </script>
</body>
</html>
