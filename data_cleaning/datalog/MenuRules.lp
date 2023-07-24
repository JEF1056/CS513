id,name,sponsor,event,venue,place,physical_description,occasion,notes,call_number,keywords,
language,date,location,location_type,currency,currency_symbol,status,page_count,dish_count

% id is the primary key
icv_id_key(ID, name, N1, N2)                 :- menu(ID, N1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
                                                menu(ID, N2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
                                                N1 < N2.
icv_id_key(ID, sponsor, S1, S2)              :- menu(ID, _, S1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _), 
                                                menu(ID, _, S2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
                                                S1 < S2.
icv_id_key(ID, event, E1, E2)                :- menu(ID, _, _, E1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
                                                menu(ID, _, _, E2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
                                                E1 < E2.
icv_id_key(ID, venue, V1, V2)                :- menu(ID, _, _, _, V1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
                                                menu(ID, _, _, _, V2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
                                                V1 < V2.
icv_id_key(ID, place, P1, P2)                :- menu(ID, _, _, _, _, P1, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
                                                menu(ID, _, _, _, _, P2, _, _, _, _, _, _, _, _, _, _, _, _, _, _),
                                                P1 < P2.
icv_id_key(ID, physical_description, D1, D2) :- menu(ID, _, _, _, _, _, D1, _, _, _, _, _, _, _, _, _, _, _, _, _),
                                                menu(ID, _, _, _, _, _, D2, _, _, _, _, _, _, _, _, _, _, _, _, _),
                                                D1 < D2.
icv_id_key(ID, occasion, O1, O2)             :- menu(ID, _, _, _, _, _, _, O1, _, _, _, _, _, _, _, _, _, _, _, _),
                                                menu(ID, _, _, _, _, _, _, O2, _, _, _, _, _, _, _, _, _, _, _, _),
                                                O1 < O2.
icv_id_key(ID, notes, N1, N2)                :- menu(ID, _, _, _, _, _, _, _, N1, _, _, _, _, _, _, _, _, _, _, _),
                                                menu(ID, _, _, _, _, _, _, _, N2, _, _, _, _, _, _, _, _, _, _, _),
                                                N1 < N2.
icv_id_key(ID, call_number, C1, C2)          :- menu(ID, _, _, _, _, _, _, _, _, C1, _, _, _, _, _, _, _, _, _, _),
                                                menu(ID, _, _, _, _, _, _, _, _, C2, _, _, _, _, _, _, _, _, _, _),
                                                C1 < C2.
icv_id_key(ID, keywords, K1, K2)             :- menu(ID, _, _, _, _, _, _, _, _, _, K1, _, _, _, _, _, _, _, _, _),
                                                menu(ID, _, _, _, _, _, _, _, _, _, K2, _, _, _, _, _, _, _, _, _),
                                                K1 < K2.
icv_id_key(ID, language, L1, L2)             :- menu(ID, _, _, _, _, _, _, _, _, _, _, L1, _, _, _, _, _, _, _, _),
                                                menu(ID, _, _, _, _, _, _, _, _, _, _, L2, _, _, _, _, _, _, _, _),
                                                L1 < L2.
icv_id_key(ID, date, D1, D2)                 :- menu(ID, _, _, _, _, _, _, _, _, _, _, _, D1, _, _, _, _, _, _, _),
                                                menu(ID, _, _, _, _, _, _, _, _, _, _, _, D2, _, _, _, _, _, _, _),
                                                D1 < D2.
icv_id_key(ID, location, L1, L2)             :- menu(ID, _, _, _, _, _, _, _, _, _, _, _, _, L1, _, _, _, _, _, _),
                                                menu(ID, _, _, _, _, _, _, _, _, _, _, _, _, L2, _, _, _, _, _, _),
                                                L1 < L2.
icv_id_key(ID, location_type, T1, T2)        :- menu(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, T1, _, _, _, _, _),
                                                menu(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, T2, _, _, _, _, _),
                                                T1 < T2.
icv_id_key(ID, currency, C1, C2)             :- menu(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, C1, _, _, _, _),
                                                menu(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, C2, _, _, _, _),
                                                C1 < C2.
icv_id_key(ID, currency_symbol, Y1, Y2)      :- menu(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, Y1, _, _, _),
                                                menu(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, Y2, _, _, _),
                                                Y1 < Y2.
icv_id_key(ID, status, S1, S2)               :- menu(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, S1, _, _),
                                                menu(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, S2, _, _),
                                                S1 < S2.
icv_id_key(ID, page_count, P1, P2)           :- menu(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, P1, _),
                                                menu(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, P2, _),
                                                P1 < P2.
icv_id_key(ID, dish_count, D1, D2)           :- menu(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, D1),
                                                menu(ID, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, D2),
                                                D1 < D2.