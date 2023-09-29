const express = require("express");
const mongoose = require("mongoose");
const swaggerJSDoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');

const app = express();
const port = 3000;

// MongoDB 연결 설정
mongoose.connect("mongodb://localhost/userDB", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// MongoDB 모델 정의
const User = mongoose.model("User", {
  username: String,
  email: String,
  // 다른 필드들도 추가할 수 있습니다.
});

// 미들웨어 설정
app.use(express.json());

// Swagger 설정
const swaggerOptions = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "User API",
      version: "1.0.0",
      description: "API for managing users",
    },
    servers: [
      {
        url: "http://localhost:3000",
        description: "Development server",
      },
    ],
  },
  apis: ["./app.js"], // 현재 파일의 경로
};

const swaggerSpec = swaggerJSDoc(swaggerOptions);

app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerSpec));

/**
 * @swagger
 * /api/profile/{username}:
 *   get:
 *     summary: Get user profile by username
 *     parameters:
 *       - in: path
 *         name: username
 *         schema:
 *           type: string
 *         required: true
 *         description: Username of the user
 *     responses:
 *       200:
 *         description: Successful response
 *       404:
 *         description: User not found
 */
app.get("/api/profile/:username", async (req, res) => {
  const username = req.params.username;
  try {
    const user = await User.findOne({ username });
    if (user) {
      res.status(200).json(user);
    } else {
      res.status(404).json({ message: "User not found" });
    }
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// 서버 시작
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
