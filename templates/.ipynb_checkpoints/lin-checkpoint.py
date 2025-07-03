<!DOCTYPE HTML>
<html lang="en">
<head>
    <title>Linear Equation Solver</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <style>
        body {
            margin: 0;
            padding: 2em;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(to right, #e3f2fd, #bbdefb);
            color: #0d47a1;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            min-height: 100vh;
        }

        h1 {
            font-size: 2.5em;
            margin-bottom: 1.5em;
            color: #1565c0;
        }

        form {
            background: #ffffffee;
            padding: 2em;
            border-radius: 15px;
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
            max-width: 500px;
            width: 100%;
        }

        form div {
            margin-bottom: 1.2em;
            font-size: 1.1em;
        }

        input[type="text"],
        input[type="number"],
        input {
            padding: 8px 10px;
            font-size: 1em;
            border-radius: 8px;
            border: 1px solid #90caf9;
            width: 60px;
            text-align: center;
            margin: 0 5px;
        }

        input[type="submit"] {
            background-color: #1976d2;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 1em;
            border-radius: 10px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease;
            margin-top: 1em;
        }

        input[type="submit"]:hover {
            background-color: #0d47a1;
            transform: scale(1.05);
        }

        .solution-box {
            margin-top: 2em;
            background-color: #e3f2fd;
            padding: 1em;
            border-radius: 10px;
            max-width: 400px;
            box-shadow: 0 3px 8px rgba(0,0,0,0.1);
            font-size: 1.2em;
            color: #1a237e;
        }

        @media screen and (max-width: 600px) {
            form {
                padding: 1.5em;
            }
            input {
                width: 50px;
            }
        }
    </style>
</head>

<body>

    <h1>🧠 Solve Linear Equations</h1>

    <form method="POST" action="/lin">
        <div>
            Equation 1: 
            <input name="x1" placeholder="a1"> x + 
            <input name="y1" placeholder="b1"> y = 
            <input name="z1" placeholder="c1">
        </div>

        <div>
            Equation 2: 
            <input name="x2" placeholder="a2"> x + 
            <input name="y2" placeholder="b2"> y = 
            <input name="z2" placeholder="c2">
        </div>

        <input type="submit" value="Solve">
    </form>

    {% if sol %}
        <div class="solution-box">
            ✅ Solution:<br><br>
            x = {{ sol[0] }}<br>
            y = {{ sol[1] }}
        </div>
    {% endif %}

</body>
</html>
