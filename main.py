from textblob import TextBlob

feedbacks = ['I love the app is amazing ', 
             "The experience was bad as hell", 
             "This app is really helpful",
             "Damn the app tastes like shit ",
            'Please don\'t download the app you will regret it ',
             "Barangnya jelek","Good app I love",
             "This review is specifically for the item SanDisk Extreme 128GB microSD UHS-I Card with Adapter - 160MB/s with SanDisk MobileMate USB 3.0 microSD Card Reader. My card was shipped from and sold by Amazon.com. The top review for this card would have you believe the product I received, based on physical appearance, is fake. The speed tests and H2testw program appear to indicate it achieves the advertised speeds and has the correct capacity using the bundled USB 3.0 card reader in a USB 3.0 port on my desktop Windows 10 PC. If this card is somehow fake it is quite impressive. I'm sure there are some fakes out there, but if you do decide to buy this card it might be worth performing your own tests before deeming it fake based off the looks alone (assuming it's not an incredibly obvious fake). April 18, 2020 (13 month update): card still works great. No complaints, I'm very happy with it."]

positive_feedbacks = []
negative_feedbacks = []

for feedback in feedbacks:
  feedback_polarity = TextBlob(feedback).sentiment.polarity
  if feedback_polarity>0:
    positive_feedbacks.append(feedback)
    continue
  negative_feedbacks.append(feedback)

print('Positive_feebacks Count : {}'.format(len(positive_feedbacks)))
print(positive_feedbacks)
print('Negative_feedback Count : {}'.format(len(negative_feedbacks)))
print(negative_feedbacks)