from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig


def generate_summary(input_paragraph, max_length=150):
    print("Input Paragraph Word Count: ", len(input_paragraph.split(' ')))
    # print(input_paragraph)
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)

    # Tokenize the input text
    input_ids = tokenizer.encode(input_paragraph, return_tensors="pt",
                                 max_length=512, truncation=True)

    # Generate summary using the model
    summary_ids = model.generate(input_ids, max_length=max_length,
                                 num_beams=5, length_penalty=0.6,
                                 no_repeat_ngram_size=2, early_stopping=True)

    # Decode the generated summary
    text_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return text_summary


# Example usage
original_text1 = """
Coffee is a beverage brewed from roasted coffee beans. Darkly colored, 
bitter, and slightly acidic, coffee has a stimulating effect on humans, 
primarily due to its caffeine content. It has the highest sales in the 
world market for hot drinks.[2]

The seeds of the Coffea plant's fruits are separated to produce 
unroasted green coffee beans. The beans are roasted and then ground 
into fine particles typically steeped in hot water before being filtered 
out, producing a cup of coffee. 
"""

woman_empowerment = """
Title: Empowering Women: Breaking Barriers and Fostering Equality

Introduction:

Woman empowerment is a multifaceted concept that encompasses social, economic, and political dimensions. Over the years, significant strides have been made towards promoting gender equality and empowering women worldwide. However, challenges persist, and there is still much work to be done to dismantle the barriers that hinder women's progress. This essay explores the importance of woman empowerment, its historical context, current challenges, and potential solutions to foster a more equitable and inclusive society.

Historical Context:

The struggle for woman empowerment is deeply rooted in history, with women fighting for their rights and recognition for centuries. Throughout the world, women have faced systemic discrimination, limited access to education, and restricted opportunities in various spheres of life. The suffragette movement of the late 19th and early 20th centuries marked a turning point, as women began to demand the right to vote and actively participate in civic life.

In the latter half of the 20th century, the feminist movement gained momentum, challenging traditional gender roles and advocating for equal opportunities. Legislation such as the Equal Pay Act in the United States and the Convention on the Elimination of All Forms of Discrimination Against Women (CEDAW) at the international level signaled a commitment to address gender disparities. Despite these advancements, gender-based discrimination and violence against women persist in many parts of the world.

Current Challenges:

1. Gender Pay Gap:

One of the persistent challenges in achieving woman empowerment is the gender pay gap. Globally, women continue to earn less than men for the same work, reflecting deep-seated inequalities in the workplace. Factors such as occupational segregation, stereotypes, and lack of transparency contribute to this gap, perpetuating economic disparities between men and women.

2. Limited Access to Education:

Access to education is a fundamental aspect of woman empowerment. However, in various regions, cultural norms, economic constraints, and discriminatory practices still prevent many girls from receiving quality education. Addressing this issue is crucial for breaking the cycle of poverty and ensuring that women have the knowledge and skills to participate fully in society.

3. Gender-Based Violence:

Violence against women remains a significant impediment to woman empowerment. This includes physical, sexual, and psychological violence, as well as harmful practices like female genital mutilation and forced marriages. Eradicating gender-based violence requires comprehensive efforts, including legal reforms, awareness campaigns, and support systems for survivors.

4. Underrepresentation in Leadership Roles:

Despite progress, women continue to be underrepresented in leadership positions across various sectors. This underrepresentation not only limits women's opportunities for professional growth but also perpetuates gender stereotypes. Increasing the number of women in leadership is essential for creating diverse and inclusive decision-making processes that reflect the needs and perspectives of the entire population.

5. Cultural and Societal Norms:

Deep-rooted cultural and societal norms often perpetuate gender stereotypes and restrict women's choices. These norms may dictate traditional gender roles, limiting women's autonomy and perpetuating harmful practices. Changing these entrenched beliefs requires a combination of legislative measures, education, and community engagement to challenge and transform prevailing attitudes.

Solutions and Empowerment Strategies:

1. Legislation and Policy Reforms:

Effective legislation and policy reforms are critical for promoting woman empowerment. Governments and organizations must enact and enforce laws that guarantee equal pay, protect against gender-based violence, and ensure equal opportunities in education and employment. Additionally, quotas and affirmative action policies can be implemented to address the underrepresentation of women in leadership roles.

2. Education and Skill Development:

Investing in education and skill development is a powerful tool for woman empowerment. Efforts should be made to eliminate barriers to education for girls, including addressing cultural norms and providing financial support. Moreover, vocational training and skill development programs can empower women economically, enabling them to enter and succeed in various professions.

3. Gender Sensitization Programs:

Promoting awareness and challenging gender stereotypes through gender sensitization programs is crucial. These programs can be integrated into schools, workplaces, and communities to foster a culture of respect, equality, and understanding. By challenging harmful stereotypes, society can create a more inclusive environment that values the contributions of both men and women.

4. Support Systems for Victims of Gender-Based Violence:

Creating robust support systems for victims of gender-based violence is essential. This includes accessible helplines, shelters, counseling services, and legal assistance. Additionally, public awareness campaigns can help break the silence surrounding these issues, encouraging survivors to come forward and seek help without fear of stigma or retaliation.

5. Corporate Initiatives for Gender Equality:

Businesses play a crucial role in promoting woman empowerment. Corporate initiatives such as diversity and inclusion programs, mentorship opportunities, and family-friendly policies contribute to a more equitable workplace. Companies can also conduct regular gender pay audits to identify and address disparities within their organizations.

6. Empowering Women in Leadership:

Promoting women to leadership positions is not just about equality; it also enhances organizational performance. Companies and governments should actively work towards increasing the representation of women in decision-making roles. Mentorship programs, leadership training, and networking opportunities can help women develop the skills and confidence needed to advance in their careers.

7. Community Engagement and Advocacy:

Community engagement is vital for achieving lasting change. Grassroots movements, NGOs, and community-based organizations play a crucial role in challenging harmful norms and advocating for woman empowerment. By involving communities in the conversation, sustainable change can be achieved, addressing cultural barriers and fostering a sense of collective responsibility.

Conclusion:

Woman empowerment is an ongoing journey marked by progress, challenges, and the collective efforts of individuals, communities, and governments. Achieving gender equality requires a comprehensive approach that addresses economic, social, and cultural factors. By dismantling barriers, promoting education, challenging stereotypes, and fostering inclusive policies, societies can create environments where women can thrive and contribute fully to the development and well-being of their communities. The empowerment of women is not just a matter of justice and equality; it is a fundamental prerequisite for building a sustainable and equitable future for all.
"""
summary = generate_summary(woman_empowerment)
print("---------------------------------------------------")
print("Generated Summary Word Count: ", len(summary.split(' ')))
for each in summary.split('. '):
    print(each)
