The AI-Based Currency Note Authentication System is a computer vision solution designed to automatically verify the authenticity of currency notes using advanced feature-matching techniques.
By analyzing and comparing a test currency note image with a reference genuine note image, the system identifies whether the currency is genuine or potentially counterfeit.

Using ORB (Oriented FAST and Rotated BRIEF) keypoint detection and Brute-Force Hamming Matcher (BFMatcher), the system extracts important image features from both the test and reference note images and matches them.
If the number of matched keypoints exceeds a predefined threshold, the note is classified as genuine; otherwise, it is flagged as potentially counterfeit.
