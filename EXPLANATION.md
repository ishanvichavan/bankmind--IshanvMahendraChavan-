# EXPLANATION.md

## Part 1: Dataset Insights & Exploratory Alignment (Everyone Answers)

### 1. What percentage of customers in your dataset have y = yes? What does this imbalance mean for how you'd evaluate a model?
Approximately **11.7%** of the customers in the `bank-full.csv` dataset have a target value of `y = yes`. This severe class imbalance means that standard metrics like accuracy are highly misleading; a naive baseline model that blindly guesses "no" for every single customer would achieve an 88.3% accuracy score while failing to find a single actual converter. To evaluate this model effectively, we must prioritize minority-class metrics like **Precision**, **Recall**, and the **F1-Score**, which explicitly track how accurately the engine isolates true buyers instead of relying on the dominant "no" class.

### 2. Which job category had the highest subscription rate? Does this make sense to you intuitively?
The **student** job category holds the highest relative subscription rate (hovering around 28.7%), followed closely by **retired** individuals. This makes perfect intuitive sense from a financial services perspective: students are highly receptive to establishing structured savings habits as they begin their careers and financial journeys, while retired clients possess accumulated lump-sum wealth and actively look for low-risk, guaranteed fixed-income vehicles like term deposits to preserve capital.

### 3. Which feature had the highest importance in your tree-based model? Why do you think that is?
The **`duration`** feature (the contact duration of the last call in seconds) holds the highest feature importance score in the Random Forest model. This aligns directly with standard sales and behavioral dynamics; the amount of time a customer is willing to stay on the line with a Relationship Manager serves as a direct proxy for their baseline engagement level, intent, and willingness to listen to the financial pitch.

### 4. Why is F1 a better metric than accuracy for this particular dataset?
Accuracy treats all classification errors equally, meaning a model could preserve an impressive 88% overall accuracy rate while maintaining a catastrophic 0% success rate at discovering true buyers. The F1-Score acts as the harmonic mean of Precision and Recall specifically on the minority class (`yes`), forcing the training algorithm to balance catching as many true buyers as possible (Recall) with keeping cold leads out of the pipeline (Precision), making it the most objective benchmark for real business value.

### 5. Pick one of your 5 sample predictions. Do you actually agree with the model's call, given that customer's features? Walk through your thinking.
Looking at a sample customer prediction where the model outputs **YES** with a probability score around **54%**: The customer's features show a high persistent account cash balance, zero active housing debt obligations (`housing: no`), and an extended communication conversation length (`duration > 350` seconds). I strongly agree with the model's prediction here because a consumer with zero structural debt burden and strong liquid capital who stays engaged on a sales call represents an ideal, high-intent candidate for asset-allocation products.

### 6. What would likely break first if 200 RMs were hitting your /predict endpoint simultaneously? What's one thing you'd change?
If 200 Relationship Managers (RMs) hit the server concurrently, the **single-process execution loop of a default Python Uvicorn web worker** would become a bottleneck, leading to request timeouts as synchronous CPU-bound matrix transformations stack up. To mitigate this structural threshold, I would change the deployment topology to run multiple horizontal process workers via a command like `uvicorn main:app --workers 4` paired with an asynchronous task queue like Celery or a reverse proxy like Nginx to cleanly balance incoming request traffic.

### 7. What does the LLM explanation actually add over just showing a probability score?
A raw probability score (such as `0.83`) tells a Relationship Manager *what* the model thinks, but offers no contextual utility on *how* to approach the client. The live Llama-3.3 natural language brief contextualizes the decision boundary, transforming abstract mathematical confidence levels into actionable sales strategies (e.g., instructing the RM to explicitly highlight "capital protection and financial security" because the profile shows a high bank balance matched with zero active personal loans).