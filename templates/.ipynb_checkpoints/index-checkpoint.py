<!DOCTYPE HTML>
<html lang="en">
<head>
    <title>Math Solver</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <style>
        body {
            margin: 0;
            padding: 2em;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(to bottom right, #e8f5e9, #c8e6c9);
            color: #1b5e20;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            text-align: center;
        }

        h1 {
            font-size: 3em;
            margin-bottom: 1.5em;
            color: #2e7d32;
        }

        .button-container {
            display: flex;
            flex-direction: column;
            gap: 1em;
        }

        button {
            background-color: #43a047;
            border: none;
            border-radius: 10px;
            padding: 15px 30px;
            font-size: 1.1em;
            color: white;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            width: 250px;
        }

        button:hover {
            background-color: #2e7d32;
            transform: scale(1.05);
        }

        @media screen and (max-width: 600px) {
            h1 {
                font-size: 2.2em;
            }

            button {
                width: 90%;
            }
        }
    </style>
</head>
<body>

    <h1>📐 Math Solver Portal</h1>

    <div class="button-container">
        <button onclick="location.href='lin'">Solve Linear Equation (2 variables)</button>
        <button onclick="location.href='quad'">Solve Quadratic Equation</button>
    </div>

</body>
</html>
