
select_vacancy = ("""
                    SELECT manager_name, start_at
                    FROM hr_vacancy
                    WHERE name="Кухар"
                    """)

update_vacancies = ("""
                    UPDATE hr_vacancy
                    SET manager_name="Опанас"
                    WHERE name="Кухар"
                    """)
insert_vacancy = ("""
                    INSERT INTO hr_vacancy (id, position_id, city_id, contact_one, employment, is_published, is_experienced, is_delivery, is_disability, start_at, end_at, rubric, category, name, office_id, store_id, template_id, manager_name)
                    VALUES  (76, 1, 27, "380930768886", 1, 1, 0, 1, 0, '20181220111822', '20191220111822', 2, 1, "имя", 1, 39, 1, "Nescafe")
                    """)

select_inserted_vacancies = ("""
                    SELECT manager_name
                    FROM hr_vacancy
                    WHERE id=76 OR id=77
                    """)
