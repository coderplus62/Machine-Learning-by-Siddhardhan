train_f1 = round(f1_score(y_train, train_predict)*100,2)
test_f1 = round(f1_score(y_test, test_predict)*100,2)

print(f'Train f1 score: {train_f1}%')
print(f'Test f1 score: {test_f1}%')