
import re
import json

input = "^Location: A bustling downtown café, with the aroma of freshly brewed coffee wafting through the air. The sound of clinking cups and quiet conversations fills the space. Bright sunlight streams through large windows, casting warm rays onto the wooden tables. Sarah, an eager learner in her mid-twenties, sits at a corner table, her laptop open as she prepares to dive into the world of financial literacy.^  \n^Scenario: Sarah has been handed her first paycheck from her new job. As she reviews her monthly expenses, she realizes she needs to budget wisely to ensure she can cover her bills and still save for a future trip. She digs through her shopping bags. Should she prioritize essential items or indulge in a new wardrobe?^  \n^Action one: Sarah decides to create a list of her essential items, making sure she focuses on what she truly needs, like groceries and bills.^  \n^Outcome one: By choosing essential items, Sarah finds herself with some extra cash for savings, earning +2 points. She feels accomplished and motivated to stick to her budget in the future.^  \n^Action two: Sarah throws caution to the wind and splurges on new clothes and luxury items that she doesn't necessarily need right now.^  \n^Outcome two: After her shopping spree, Sarah realizes she barely has enough left to pay her rent, losing -1 point. She learns the hard way about the importance of prioritizing essentials over nonessentials.^  \n\n^Location: The living room of her shared apartment, with colorful posters on the walls and a cozy couch that looks inviting. The room is scattered with magazines and bills, a sign of her busy life. A calendar hangs on the wall, marking important financial dates.^  \n^Scenario: With her first credit card in hand, Sarah is excited to use it for online shopping. She knows she has a limit, but the thrill of instant purchases tempts her to spend without thinking. Should she make a purchase she cannot really afford?^  \n^Action one: Sarah decides to check her bank account and ensures she can afford the items before using her credit card.^  \n^Outcome one: By being responsible and only spending what she can afford, Sarah builds her credit and earns +2 points, feeling empowered by her financial decision-making.^  \n^Action two: Sarah impulsively uses her credit card on several non-essential items, planning to avoid paying the full balance until next month.^  \n^Outcome two: In the end, Sarah faces high-interest charges and a mountain of debt that overwhelms her, losing -1 point. She learns that credit cards can lead to trouble if not used wisely.^  \n\n^Location: A local library, where rows of books fill the shelves and cozy study nooks create an inviting atmosphere. The quiet hum of knowledge inspires Sarah as she sits at a desk with her laptop, contemplating investments for her savings.^  \n^Scenario: Sarah has some savings and is trying to decide whether to invest in stocks or keep her money in a chequing account. She knows that inflation can eat away at her cash but isn’t sure which route to take.^  \n^Action one: Sarah spends time researching different stocks and their performance, considering how to make her money grow.^  \n^Outcome one: By doing proper research, she selects a promising stock that increases in value, earning +2 points. She feels empowered by the success of her informed decision.^  \n^Action two: Sarah opts to keep her money in a chequing account, thinking it’s safer and easier to access, without fully understanding inflation.^  \n^Outcome two: Over time, she realizes the value of her money has diminished due to inflation, losing -1 point. She understands now that making her money work for her is crucial.^  \n\n^Location: A bright, modern bank with glass windows that reflect the hustle of the city outside. The air smells crisp and new. Sarah sits in a comfortable chair across from a friendly bank advisor, eager to learn more about her options.^  \n^Scenario: Sarah is trying to make informed decisions about her savings and investments, relying heavily on online articles and advice. Should she ask the bank advisor for advice or base her choices solely on her research?^  \n^Action one: Sarah asks the bank advisor for guidance on her financial plans, taking advantage of their expertise.^  \n^Outcome one: The advisor provides her with invaluable insights that help her make informed choices, earning +2 points. Sarah now realizes the importance of professional guidance in managing her finances.^  \n^Action two: Sarah declines to consult the bank advisor, insisting she knows enough from her research and online recommendations.^  \n^Outcome two: Sarah makes misinformed financial decisions based solely on her limited research, resulting in a poor investment choice, losing -1 point. She learns the hard way the value of expert advice.^  \n\n^Location: A community workshop space decorated with inspiring quotes and motivational posters. The scent of fresh paint lingers in the air as people gather to discuss entrepreneurship and the excitement of starting a business. Sarah is keenly interested in starting her own shop.^  \n^Scenario: Sarah dreams of launching an online craft store but isn’t sure whether to take out a loan to get it started quickly or save up cash over time, potentially delaying her business launch. What should she choose?^  \n^Action one: Sarah decides to take out a small loan to cover initial inventory and setup costs, believing it will give her the chance to establish her business sooner.^  \n^Outcome one: With the loan, she launches her shop quickly and successfully captures a market, earning +2 points. She feels exhilarated and grateful for the swift decision.^  \n^Action two: Sarah chooses to save up all the funds she needs before starting her business, believing it’s the safer route, but she misses out on current market opportunities.^  \n^Outcome two: While her intentions were noble, her prolonged wait leads to lost customers and decreased excitement for her product launch, losing -1 point. She understands the necessity of calculated risks in business.^  \n\n^Location: Sarah's chic little store, filled with vibrant products displayed on shelves and a palpable energy in the air from her growing e-commerce brand. The sounds of typing and notifications from her online store add to the excitement. She’s been revamping her strategy.^  \n^Scenario: Sarah’s physical store has gained traction, but she’s considering whether to fully embrace e-commerce to reach a wider audience or stick to traditional sales methods. How should she proceed?^  \n^Action one: Sarah recognizes the potential of embracing e-commerce and takes steps to enhance her online sales platform.^  \n^Outcome one: By successfully expanding her online presence, her sales skyrocket and she increases her customer base, earning +2 points. Sarah realizes the value of adapting to modern shopping habits.^  \n^Action two: Sarah decides to prioritize her in-person sales and remain with cash transactions, thinking it’s simpler and avoids tech issues.^  \n^Outcome two: As time goes by, Sarah struggles to keep her sales afloat as competitors dominate the online market, losing -1 point. She learns that adaptability is crucial for business success in a digital age.^ "

def list_to_json(data_list):
    result = {str(i+1): data_list[i] for i in range(len(data_list))}
    return json.dumps(result, indent=2)


def split_string(input_string):
    parts = re.split(r'[\^:]', input_string)
    return [part.strip() for part in parts if part.strip()]


def remove_unicode_escape(string: str) -> str:
    """
    Replaces any occurrence of '\u' followed by 5 characters
    with a single space.
    """
    return re.sub(r"\\u.{5}", " ", input_string)
# Example usage:
test_str = "Hello \\u12345World"
print(remove_unicode_escape(test_str))