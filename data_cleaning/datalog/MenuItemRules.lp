% menuitem(id, menu_page_id, price, high_price, dish_id, created_at, updated_at, xpos, ypos)

% id is the primary key
icv_id_key(ID, menu_page, M1, M2)  :- menuitem(ID, M1, _, _, _, _, _, _, _), menuitem(ID, M2, _, _, _, _, _, _, _), M1 < M2.
icv_id_key(ID, price, P1, P2)      :- menuitem(ID, _, P1, _, _, _, _, _, _), menuitem(ID, _, P2, _, _, _, _, _, _), P1 < P2.
icv_id_key(ID, high_price, H1, H2) :- menuitem(ID, _, _, H1, _, _, _, _, _), menuitem(ID, _, _, H2, _, _, _, _, _), H1 < H2.
icv_id_key(ID, dish_id, D1, D2)    :- menuitem(ID, _, _, _, D1, _, _, _, _), menuitem(ID, _, _, _, D2, _, _, _, _), D1 < D2.
icv_id_key(ID, created_at, C1, C2) :- menuitem(ID, _, _, _, _, C1, _, _, _), menuitem(ID, _, _, _, _, C2, _, _, _), C1 < C2.
icv_id_key(ID, updated_at, U1, U2) :- menuitem(ID, _, _, _, _, _, U1, _, _), menuitem(ID, _, _, _, _, _, U2, _, _), U1 < U2.
icv_id_key(ID, xpos, X1, X2)       :- menuitem(ID, _, _, _, _, _, _, X1, _), menuitem(ID, _, _, _, _, _, _, X2, _), X1 < X2.
icv_id_key(ID, xpos, Y1, Y2)       :- menuitem(ID, _, _, _, _, _, _, _, Y1), menuitem(ID, _, _, _, _, _, _, _, Y2), Y1 < Y2.

% created_at should be greater than 2011
icv_created_at(ID, CA) :- menuitem(ID, _, _, _, _, CA, _, _, _), CA < "2011".

% created_at should be less than updated_at
icv_createdat_updatedat(ID, CA, UA) :- menuitem(ID, _, _, _, _, CA, UA, _, _), UA < CA.