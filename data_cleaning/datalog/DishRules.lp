% dish(id, name, description, menus_appeared, times_appeared, first_appeared, last_appeared, lowest_price, highest_price)

% id is the primary key
icv_id_key(ID, name, N1, N2)           :- dish(ID, N1, _, _, _, _, _, _, _), dish(ID, N2, _, _, _, _, _, _, _), N1 < N2.
icv_id_key(ID, description, D1, D2)    :- dish(ID, _, D1, _, _, _, _, _, _), dish(ID, _, D2, _, _, _, _, _, _), D1 < D2.
icv_id_key(ID, menus_appeared, M1, M2) :- dish(ID, _, _, M1, _, _, _, _, _), dish(ID, _, _, M2, _, _, _, _, _), M1 < M2.
icv_id_key(ID, times_appeared, T1, T2) :- dish(ID, _, _, _, T1, _, _, _, _), dish(ID, _, _, _, T2, _, _, _, _), T1 < T2.
icv_id_key(ID, first_appeared, F1, F2) :- dish(ID, _, _, _, _, F1, _, _, _), dish(ID, _, _, _, _, F2, _, _, _), F1 < F2.
icv_id_key(ID, last_appeared, L1, L2)  :- dish(ID, _, _, _, _, _, L1, _, _), dish(ID, _, _, _, _, _, L2, _, _), L1 < L2.
icv_id_key(ID, lowest_price, X1, X2)   :- dish(ID, _, _, _, _, _, _, X1, _), dish(ID, _, _, _, _, _, _, X2, _), X1 < X2.
icv_id_key(ID, highest_price, Y1, Y2)  :- dish(ID, _, _, _, _, _, _, _, Y1), dish(ID, _, _, _, _, _, _, _, Y2), Y1 < Y2.

% first_appeared should be before last_appeared
icv_firstappeared_lastappeared(ID, FA, LA) :- dish(ID, _, _, _, _, FA, LA, _, _), LA < FA.

% lowest_price should be less than highest_price
icv_lowestprice_highestprice(ID, LP, HP) :- dish(ID, _, _, _, _, _, _, LP, HP), LP > HP.

% times_appeared should be greater or equal to menus_appeared
icv_timesappeared_menusappeared(ID, MA, TA) :- dish(ID, _, _, MA, TA), MA < TA.

% Generated from InputDishCleaned.csv
dish(1, "Consomme, Printaniere Royal", "Consomme Printaniere Royal", 10, 8, 1897, 1927, "0", "0").
dish(2, "Chicken Gumbo", "Chicken Gumbo", 111, 117, 1895, 1960, "0", "0").