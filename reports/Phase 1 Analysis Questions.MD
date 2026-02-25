# **Analysis Questions**

1. Which data source (structured, behavioral, or audio) is most predictive of performance?

    Answer
    
    The structured quantitative metrics data source (structured_data․csv + Random Forest model) is clearly the most predictive of employee performance․

    Structured data Random Forests: 91․9% to 92% test accuracy
    Logistic Regression (Behavioral logs) → Test accuracy ≈ 55․5%
    Audio features (SVC with RBF kernel) → Test accuracy: 56․7%

    Gap explanation:
    The structured data contains direct, outcome-oriented quantitative measures (e․g․ efficiency_score, innovation_score, client_satisfaction_score, deadline_met_score) which are conceptually very close to standard metrics used to assess organization-wide performance․ Thus, we see a much stronger signal → ~92% test accuracy․
    Behavioral and audio features are more indirect / noisy proxies that seem to contain information, but by themselves are far less discriminative for the final performance rating․
   
2. Are any models showing signs of overfitting? How can you tell?

    Answer
    Random Forest (structured) → moderate overfitting
    
    → Train accuracy is perfect (100%), test is excellent but still ~8% lower.
    → This is typical behavior for untuned Random Forest on tabular data — it memorizes the training set very well.
    → Still generalizes strongly (92% is very good), so overfitting is present but not catastrophic.
    Logistic Regression (behavioral) & SVC (audio) → no meaningful overfitting.
    → Train and test accuracies are almost the same (gap < 2%).
    → These models are actually underfitting — they cannot capture the patterns well even on training data.

    Conclusion:
    Only the Random Forest model shows signs of moderate overfitting. The other two models are underfitting / too weak.

3. Which performance class (High, Medium, Low) is hardest to predict for each model?

    Answer
    Medium performance is the hardest class to predict, even though the dataset is perfectly balanced (~33.3% each).
    This is a classic sign that Medium is the boundary / transition class — models have more difficulty drawing clean decision boundaries around it.

4. Do you see any patterns in misclassifications?

   Answer
   Main misclassification patterns observed (from confusion matrices):

   Medium is frequently confused with both Low and High
   → Medium acts as a "bridge" class — many employees who are borderline get pulled toward Low or High depending on a few strong features.
   Strong directional bias in the weaker models (behavioral & audio):
   Logistic Regression (behavioral) and SVC (audio) both tend to over-predict Medium
   → A large number of actual High and Low employees are incorrectly classified as Medium.
   → This is typical when a model is weak / linear — it collapses toward the average / central class.

   Random Forest (structured) shows much cleaner separation, but still has:
   Low → Medium confusion > Low → High
   High → Medium confusion > High → Low
   → Even the strong model struggles most with the boundary cases around Medium.



